document.addEventListener('DOMContentLoaded', () => {
    const btnGen = document.getElementById('btn-generate');
    const btnYaml = document.getElementById('btn-yaml');
    const btnCopy = document.getElementById('btn-copy');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const output = document.getElementById('output');
    const nodeCount = document.getElementById('node-count');
    
    let allNodes = [];

    // 加载节点数据
    async function loadNodes() {
        loading.classList.remove('hidden');
        try {
            // 假设 CI 会将节点数据导出到 web/nodes.json
            const resp = await fetch('nodes.json?t=' + Date.now()); 
            allNodes = await resp.json();
            console.log(`Loaded ${allNodes.length} nodes.`);
        } catch (e) {
            alert('加载节点数据失败，请确保 nodes.json 存在。');
            console.error(e);
        } finally {
            loading.classList.add('hidden');
        }
    }

    function filterNodes() {
        const regions = document.getElementById('regions').value.toUpperCase().split(',').map(s => s.trim()).filter(Boolean);
        const protocols = document.getElementById('protocols').value.toLowerCase().split(',').map(s => s.trim()).filter(Boolean);

        return allNodes.filter(n => {
            if (regions.length > 0 && !regions.includes((n.region || '').toUpperCase())) return false;
            if (protocols.length > 0 && !protocols.includes((n.protocol || '').toLowerCase())) return false;
            return true;
        });
    }

    function generateBase64(nodes) {
        const urls = nodes.map(n => n.url).filter(Boolean);
        return btoa(urls.join('\n'));
    }

    function generateClashYaml(nodes) {
        // 极简 Clash YAML 生成
        let yaml = "port: 7890\nsocks-port: 7891\nallow-lan: false\nmode: rule\nlog-level: info\nproxies:\n";
        nodes.forEach(n => {
            if (n.clash_yaml) yaml += n.clash_yaml + "\n";
        });
        yaml += "proxy-groups:\n  - name: AutoNodes\n    type: select\n    proxies:\n";
        nodes.forEach(n => {
            yaml += `      - ${n.name || n.tag}\n`;
        });
        yaml += "rules:\n  - MATCH,AutoNodes\n";
        return yaml;
    }

    async function handleGenerate(format) {
        if (allNodes.length === 0) await loadNodes();
        if (allNodes.length === 0) return;

        loading.classList.remove('hidden');
        result.classList.add('hidden');
        
        // 使用 setTimeout 让 UI 有机会更新
        setTimeout(() => {
            const filtered = filterNodes();
            nodeCount.textContent = filtered.length;
            
            if (filtered.length === 0) {
                output.value = "未找到匹配的节点。";
            } else {
                output.value = format === 'base64' ? generateBase64(filtered) : generateClashYaml(filtered);
            }
            
            loading.classList.add('hidden');
            result.classList.remove('hidden');
        }, 50);
    }

    btnGen.addEventListener('click', () => handleGenerate('base64'));
    btnYaml.addEventListener('click', () => handleGenerate('yaml'));
    
    btnCopy.addEventListener('click', () => {
        output.select();
        document.execCommand('copy');
        btnCopy.textContent = '已复制!';
        setTimeout(() => btnCopy.textContent = '复制到剪贴板', 2000);
    });

    loadNodes();
});
