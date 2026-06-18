# Cloudflare Worker 订阅加速方案

## 背景

当前项目通过 GitHub Raw 和 jsDelivr CDN 分发订阅文件。但 jsDelivr 有缓存延迟（最长可达数小时），且在某些地区访问不稳定。

Cloudflare Worker 提供了免费的边缘计算能力，可以作为替代或补充 CDN 方案。

## 方案

### Worker 脚本

```javascript
// cloudflare-worker/sub-proxy.js
// 部署到 Cloudflare Worker 后，可直接代理 GitHub Raw 订阅文件
// 优势：全球边缘节点、无缓存延迟、免费额度 10万次/天

const GITHUB_RAW = "https://raw.githubusercontent.com/LeilaoMi/AutoMergePublicNodes-Optimized/main/output";

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;

    // 映射路径
    const fileMap = {
      "/verified.txt": `${GITHUB_RAW}/verified.txt`,
      "/verified.yaml": `${GITHUB_RAW}/verified.yaml`,
      "/verified.json": `${GITHUB_RAW}/verified.json`,
      "/global.txt": `${GITHUB_RAW}/global.txt`,
      "/global.yaml": `${GITHUB_RAW}/global.yaml`,
      "/global.json": `${GITHUB_RAW}/global.json`,
      "/all.txt": `${GITHUB_RAW}/all.txt`,
      "/health_report.md": `${GITHUB_RAW}/health_report.md`,
      "/stats.json": `${GITHUB_RAW}/stats.json`,
    };

    const target = fileMap[path];
    if (!target) {
      return new Response("Not found. Available: " + Object.keys(fileMap).join(", "), {
        status: 404,
        headers: { "Content-Type": "text/plain" },
      });
    }

    const resp = await fetch(target, { cf: { cacheTtl: 300 } });

    // 添加跨域和内容类型头
    const headers = new Headers(resp.headers);
    headers.set("Access-Control-Allow-Origin", "*");
    headers.set("Cache-Control", "public, max-age=300");

    return new Response(resp.body, { status: resp.status, headers });
  },
};
```

### 部署步骤

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Workers & Pages → Create Application → Create Worker
3. 命名为 `sub-proxy`（或任意名称）
4. 粘贴上面的脚本
5. 部署

### 使用方式

部署后，用户可以用以下地址替代 GitHub Raw：

```text
https://sub-proxy.<your-subdomain>.workers.dev/verified.txt
https://sub-proxy.<your-subdomain>.workers.dev/verified.yaml
https://sub-proxy.<your-subdomain>.workers.dev/health_report.md
```

### 与 jsDelivr 对比

| 特性 | GitHub Raw | jsDelivr CDN | Cloudflare Worker |
|---|---|---|---|
| 缓存延迟 | 无 | 数小时 | 可控（5 分钟） |
| 全球加速 | 否 | 是 | 是（边缘节点） |
| 免费额度 | 无限 | 无限 | 10 万次/天 |
| 中国可达性 | 差 | 中等 | 好 |
| 自定义域名 | 否 | 否 | 是 |

### 可选：绑定自定义域名

在 Cloudflare Dashboard 中：
1. Workers → sub-proxy → Triggers → Custom Domains
2. 添加如 `sub.yourdomain.com`
3. 用户即可通过 `https://sub.yourdomain.com/verified.txt` 访问

## 注意事项

- Cloudflare Worker 免费版每天 10 万次请求，对个人项目足够
- Worker 脚本中的 `cacheTtl: 300` 设置 5 分钟缓存，平衡新鲜度和性能
- 如果流量增大，可升级到 Workers Paid（$5/月，1000 万次请求）