# AutoMergePublicNodes

自动合并公开代理节点，生成多格式订阅。

## 特性

- 支持 vmess, ss, ssr, trojan, vless, hysteria2 协议
- TCP 连通性测试过滤无效节点
- 自动生成 Clash/Meta/V2Ray 订阅
- 按地区分类节点
- 定时自动更新（每12小时）

## 订阅链接

| 格式 | 链接 |
|------|------|
| V2Ray | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/list.txt` |
| Clash | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/list.yml` |
| Meta | `https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/list.meta.yml` |

## 本地运行

```bash
pip install -r requirements.txt
python3 fetch.py    # 获取节点
python3 filter.py   # TCP 测试过滤
```

## 配置

- `sources.list` - 订阅源列表
- `config.yml` - Clash 配置模板
- `snippets/_config.yml` - 地区分类配置
