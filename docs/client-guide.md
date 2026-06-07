# 客户端导入指南

本项目输出分三类：

| 输出 | 适合人群 | 说明 |
|---|---|---|
| `output/verified.*` | 质量优先 | GitHub Actions 环境下 sing-box 真测通过，数量可能较少 |
| `output/global.*` | 数量与质量兼顾 | 海外可用但国内站点连通不一定稳定 |
| `output/all.*` | 自己再测速 | 全量候选池，只去重，不保证可用 |
| `output/local_verified.*` | 本地用户 | 运行 `tools/local_filter.py` 后生成，更贴近你的网络环境 |

> 建议普通用户优先导入 `verified.yaml` 或 `verified.txt`；如果数量太少，再尝试 `global.*`。

---

## Clash / Mihomo / Clash Verge Rev

推荐文件：

```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.yaml
```

备用：

```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/global.yaml
```

使用建议：

1. 新建订阅配置。
2. 粘贴 `verified.yaml` 链接。
3. 更新订阅。
4. 先使用内置 `♻️ Auto` 分组或按地区分组测速。
5. 如果节点少或不可用，切换到 `global.yaml`。

---

## v2rayN / v2rayNG

推荐文件：

```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.txt
```

备用：

```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/global.txt
```

说明：

- `.txt` 是 base64 订阅，适合 v2rayN / v2rayNG 等通用订阅客户端。
- 如果客户端支持 URL 列表，也可以导入 `.urls`。

---

## Karing / sing-box

推荐文件：

```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/verified.json
```

备用：

```text
https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output/global.json
```

说明：

- `.json` 是 sing-box 配置结构，已带 selector / url-test / DNS / route。
- Karing 如果导入失败，可以改用 `.txt` 或 `.yaml` 后通过订阅转换。

---

## Shadowrocket / Quantumult X / Loon / Surge

优先使用转换链接：

```text
output/verified.converter.md
output/global.converter.md
```

注意：

- 第三方订阅转换服务可能不可用，也可能记录你的订阅 URL。
- 更稳妥的方式是本地搭建 subconverter。
- 如果只想快速使用，可先从 `verified.converter.md` 选择对应客户端目标格式。

---

## 本地二次筛选

GitHub Actions 的测试环境一般在海外机房，不等于你的本地网络可用。可以运行：

```bash
python tools/local_filter.py --input output/global.urls --output-prefix local_verified --top-n 100
```

生成：

```text
output/local_verified.txt
output/local_verified.urls
output/local_verified.yaml
output/local_verified.json
```

如果只想生成轻量输出：

```bash
python tools/local_filter.py --input output/all.txt --output-mode light --top-n 200
```

---

## 常见问题

### verified 数量很少，是不是项目坏了？

通常不是。公共节点波动大，且本项目筛选严格：TCP 可达后还要通过 sing-box 真实代理测试。

### 导入 Clash 后所有节点都不能用？

建议按顺序检查：

1. 更新订阅是否成功。
2. 系统时间是否正确。
3. 客户端内核是否支持 VLESS / Reality / Hysteria2 / TUIC。
4. 尝试 `global.yaml`。
5. 运行 `tools/local_filter.py` 做本地筛选。

### 为什么 all.* 数量多但很多不可用？

`all.*` 是候选池，主要给用户或第三方工具再测速，不代表真实可用。