# AutoMergePublicNodes - 优化版

自动合并公开代理节点，生成多格式订阅。

## 特性

- ✅ **异步并发** - 使用 asyncio 实现高效并发获取
- ✅ **多协议支持** - vmess, ss, ssr, trojan, vless, hysteria2
- ✅ **动态日期URL** - 支持 `+date` 格式自动填充日期
- ✅ **订阅列表递归** - 支持 `*` 前缀递归获取订阅列表
- ✅ **TCP连通性测试** - 异步测试过滤无效节点
- ✅ **多格式输出** - V2Ray, Clash, Meta
- ✅ **按地区分类** - 自动按节点名称分类
- ✅ **CDN加速** - 自动转换为 JsDelivr 链接

## 快速开始

### 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行
python main.py

# 指定参数
python main.py -n 300 --no-tcp-test
```

### GitHub Actions 部署

1. **Fork 本仓库**

2. **修改订阅源**（可选）
   编辑 `config/sources.list`，添加你的订阅链接

3. **启用 Actions**
   进入 Settings → Actions → General → Allow all actions

4. **手动触发测试**
   Actions → Update Nodes → Run workflow

## 订阅源配置语法

`config/sources.list` 支持以下格式：

| 前缀 | 说明 | 示例 |
|------|------|------|
| 无 | 普通订阅 | `https://example.com/sub` |
| `!` | 国内无法访问 | `!https://...` |
| `+date` | 动态日期URL | `+date https://example.com/%Y/%m/%Y%m%d.txt` |
| `*` | 订阅列表 | `*https://...` |
| `#max=N` | 限制节点数 | `https://...#max=100` |
| `#ignore=A,B` | 忽略协议 | `https://...#ignore=ss,ssr` |

示例：

```
# 普通订阅
https://raw.githubusercontent.com/user/repo/main/clash.yaml

# 动态日期（每天更新）
+date https://nodefree.org/dy/%Y/%m/%Y%m%d.txt

# 订阅列表（抓取后每行又是一个订阅）
*https://raw.githubusercontent.com/user/list/main/README.md

# 带参数
https://example.com/sub#max=50&ignore=ssr

# 注释
# https://disabled.com/sub
```

## 命令行参数

```bash
python main.py --help

Options:
  -s, --sources PATH     订阅源配置文件 [default: config/sources.list]
  -c, --config PATH      Clash 配置模板 [default: config/config.yaml]
  -o, --output PATH      输出目录 [default: output]
  -n, --max-nodes INT    最大节点数 [default: 200]
  -t, --timeout INT      获取超时(秒) [default: 10]
  --concurrent INT       并发获取数 [default: 20]
  --no-tcp-test          跳过 TCP 连通性测试
  --tcp-timeout INT      TCP 测试超时(秒) [default: 5]
  --tcp-concurrent INT   TCP 测试并发数 [default: 100]
  --no-dynamic           跳过动态源
  -v, --verbose          详细输出
```

## 目录结构

```
.
├── .github/workflows/
│   └── update.yml        # GitHub Actions 配置
├── config/
│   ├── config.yaml       # Clash 配置模板
│   └── sources.list      # 订阅源列表
├── output/               # 输出目录
│   ├── list.txt          # V2Ray 订阅
│   ├── list.yml          # Clash 订阅
│   ├── list.meta.yml     # Meta 订阅
│   └── README.md         # 统计信息
├── snippets/
│   └── _config.yml       # 分类配置
├── src/
│   ├── node.py           # 节点模型
│   ├── fetcher.py        # 异步获取器
│   ├── filter.py         # TCP 测试
│   ├── generator.py      # 订阅生成
│   └── dynamic.py        # 动态源
├── main.py               # 主程序
├── requirements.txt
└── README.md
```

## 与原版对比

| 功能 | 原版 | 优化版 |
|------|------|--------|
| 并发模型 | threading | asyncio |
| 代码结构 | 单文件1000行 | 模块化 |
| 类型注解 | 部分 | 完整 |
| 错误处理 | 裸 except | 精确捕获 |
| 配置管理 | 散落代码 | 集中管理 |
| 日志系统 | print | logging |
| 进度显示 | 基础 | 增强 |

## 订阅链接

运行成功后，订阅文件在 `output/` 目录：

| 格式 | 链接 |
|------|------|
| V2Ray | `https://raw.githubusercontent.com/你的用户名/AutoMergePublicNodes/main/output/list.txt` |
| Clash | `https://raw.githubusercontent.com/你的用户名/AutoMergePublicNodes/main/output/list.yml` |
| Meta | `https://raw.githubusercontent.com/你的用户名/AutoMergePublicNodes/main/output/list.meta.yml` |

## License

MIT
