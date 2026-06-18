"""v2.6 Self-Healing System 测试"""
import sys
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from core._self_healing import SelfHealingSystem, HealingReport


def test_self_healing_init():
    """测试自愈系统初始化"""
    print("测试自愈系统初始化...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        assert healer.output_dir == Path(tmpdir)
        assert healer.actions_log == Path(tmpdir) / "healing_actions.json"
        print("✓ 自愈系统初始化成功")


def test_detect_dead_sources():
    """测试死源检测"""
    print("测试死源检测...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 测试数据：包含死源
        stats = {
            "source_scores": {
                "https://good-source.com": {
                    "score": 0.8,
                    "consecutive_dead": 0,
                },
                "https://bad-source-1.com": {
                    "score": 0.05,  # 低分
                    "consecutive_dead": 0,
                },
                "https://bad-source-2.com": {
                    "score": 0.5,
                    "consecutive_dead": 5,  # 连续失败5次
                },
                "https://good-source-2.com": {
                    "score": 0.9,
                    "consecutive_dead": 1,
                },
            }
        }
        
        dead_sources = healer._detect_dead_sources(stats)
        
        assert len(dead_sources) == 2
        assert "https://bad-source-1.com" in dead_sources
        assert "https://bad-source-2.com" in dead_sources
        assert "https://good-source.com" not in dead_sources
        assert "https://good-source-2.com" not in dead_sources
        
        print(f"✓ 死源检测成功：发现 {len(dead_sources)} 个死源")


def test_auto_disable_source():
    """测试自动禁用源"""
    print("测试自动禁用源...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # 创建临时 sources.yaml
        sources_yaml = Path(tmpdir) / "sources.yaml"
        sources_yaml.write_text("""
sources:
  - url: https://good-source.com
    enabled: true
  - url: https://bad-source.com
    enabled: true
  - url: https://another-source.com
    enabled: true
""", encoding='utf-8')
        
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 禁用坏源
        action = healer._auto_disable_source(
            "https://bad-source.com",
            str(sources_yaml)
        )
        
        assert action.success == True
        assert action.action_type == "disable_source"
        assert action.target == "https://bad-source.com"
        
        # 验证文件已更新
        import yaml
        with open(sources_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        sources = data["sources"]
        bad_source = [s for s in sources if s["url"] == "https://bad-source.com"][0]
        assert bad_source["enabled"] == False
        
        good_source = [s for s in sources if s["url"] == "https://good-source.com"][0]
        assert good_source["enabled"] == True
        
        print("✓ 自动禁用源成功")


def test_auto_add_source():
    """测试自动添加源"""
    print("测试自动添加源...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # 创建临时 sources.yaml
        sources_yaml = Path(tmpdir) / "sources.yaml"
        sources_yaml.write_text("""
sources:
  - url: https://existing-source.com
    enabled: true
""", encoding='utf-8')
        
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 添加新源
        action = healer._auto_add_source(
            "https://new-source.com",
            str(sources_yaml)
        )
        
        assert action.success == True
        assert action.action_type == "add_source"
        assert action.target == "https://new-source.com"
        
        # 验证文件已更新
        import yaml
        with open(sources_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        sources = data["sources"]
        assert len(sources) == 2
        
        new_source = [s for s in sources if s["url"] == "https://new-source.com"][0]
        assert new_source["enabled"] == True
        
        print("✓ 自动添加源成功")


def test_auto_add_duplicate_source():
    """测试添加重复源"""
    print("测试添加重复源...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # 创建临时 sources.yaml
        sources_yaml = Path(tmpdir) / "sources.yaml"
        sources_yaml.write_text("""
sources:
  - url: https://existing-source.com
    enabled: true
""", encoding='utf-8')
        
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 尝试添加已存在的源
        action = healer._auto_add_source(
            "https://existing-source.com",
            str(sources_yaml)
        )
        
        assert action.success == True  # 操作成功，但有警告
        assert "warning" in action.details
        
        # 验证文件未改变
        import yaml
        with open(sources_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        sources = data["sources"]
        assert len(sources) == 1  # 仍然是1个
        
        print("✓ 添加重复源处理正确")


def test_scoring_needs_tuning():
    """测试评分调优判断"""
    print("测试评分调优判断...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 测试低通过率
        stats_low = {
            "nodes_real_ok": 5,
            "nodes_tcp_ok": 100,
        }
        assert healer._scoring_needs_tuning(stats_low) == True  # 5% 通过率
        
        # 测试高通过率
        stats_high = {
            "nodes_real_ok": 95,
            "nodes_tcp_ok": 100,
        }
        assert healer._scoring_needs_tuning(stats_high) == True  # 95% 通过率
        
        # 测试正常通过率
        stats_normal = {
            "nodes_real_ok": 50,
            "nodes_tcp_ok": 100,
        }
        assert healer._scoring_needs_tuning(stats_normal) == False  # 50% 通过率
        
        # 测试无TCP节点
        stats_no_tcp = {
            "nodes_real_ok": 0,
            "nodes_tcp_ok": 0,
        }
        assert healer._scoring_needs_tuning(stats_no_tcp) == False
        
        print("✓ 评分调优判断正确")


def test_optimize_test_schedule():
    """测试测试策略优化"""
    print("测试测试策略优化...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 测试大量节点
        stats_many = {
            "nodes_tcp_ok": 1500,
        }
        action = healer._optimize_test_schedule(stats_many)
        
        assert action is not None
        assert action.action_type == "optimize_schedule"
        assert "suggested_concurrency" in action.details
        assert action.details["suggested_concurrency"] <= 100
        
        # 测试少量节点
        stats_few = {
            "nodes_tcp_ok": 500,
        }
        action = healer._optimize_test_schedule(stats_few)
        
        assert action is None  # 不需要优化
        
        print("✓ 测试策略优化正确")


def test_save_actions_log():
    """测试动作日志保存"""
    print("测试动作日志保存...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 创建报告
        report = HealingReport(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            actions=[],
            health_before={"test": "before"},
            health_after={"test": "after"},
        )
        
        # 保存日志
        healer._save_actions_log(report)
        
        # 验证文件已创建
        assert healer.actions_log.exists()
        
        # 验证内容
        import json
        with open(healer.actions_log, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
        
        assert len(log_data) == 1
        assert log_data[0]["timestamp"] == report.timestamp
        assert log_data[0]["health_before"] == report.health_before
        
        print("✓ 动作日志保存成功")


def test_full_analyze_and_heal():
    """测试完整的自愈流程"""
    print("测试完整自愈流程...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # 创建临时 sources.yaml
        sources_yaml = Path(tmpdir) / "sources.yaml"
        sources_yaml.write_text("""
sources:
  - url: https://good-source.com
    enabled: true
  - url: https://bad-source.com
    enabled: true
""", encoding='utf-8')
        
        healer = SelfHealingSystem(output_dir=tmpdir)
        
        # 模拟统计数据
        stats = {
            "source_scores": {
                "https://good-source.com": {
                    "score": 0.8,
                    "consecutive_dead": 0,
                },
                "https://bad-source.com": {
                    "score": 0.05,
                    "consecutive_dead": 0,
                },
            },
            "sources_total": 2,
            "sources_healthy": 1,
            "nodes_real_ok": 50,
            "nodes_verified_output": 45,
            "degraded_mode": False,
        }
        
        # 执行自愈
        report = healer.analyze_and_heal(
            sources_yaml=str(sources_yaml),
            stats=stats,
        )
        
        # 验证报告
        assert isinstance(report, HealingReport)
        assert len(report.actions) >= 1  # 至少禁用了坏源
        
        # 验证坏源已被禁用
        import yaml
        with open(sources_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        sources = data["sources"]
        bad_source = [s for s in sources if s["url"] == "https://bad-source.com"][0]
        assert bad_source["enabled"] == False
        
        # 验证日志已保存
        assert healer.actions_log.exists()
        
        print(f"✓ 完整自愈流程成功：执行了 {len(report.actions)} 个动作")


def run_all_tests():
    """运行所有测试"""
    print("\n" + "="*60)
    print("v2.6 Self-Healing System 测试套件")
    print("="*60 + "\n")
    
    tests = [
        test_self_healing_init,
        test_detect_dead_sources,
        test_auto_disable_source,
        test_auto_add_source,
        test_auto_add_duplicate_source,
        test_scoring_needs_tuning,
        test_optimize_test_schedule,
        test_save_actions_log,
        test_full_analyze_and_heal,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} 失败: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
        print()
    
    print("="*60)
    print(f"测试结果: {passed} 通过, {failed} 失败")
    print("="*60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)