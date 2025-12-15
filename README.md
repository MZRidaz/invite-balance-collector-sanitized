
# Invite Balance Collector

## English

Invite Balance Collector is a Playwright-based automation framework for collecting
invite / referral wallet balances from multiple websites and aggregating them into Excel.

### Features
- Modular site plugins
- Playwright browser automation
- Excel aggregation
- Windows / Linux support
- Safe for GitHub (no secrets included)

### Installation
```bash
pip install -r requirements.txt
playwright install
```

### Usage
1. Copy configuration template:
```bash
cp config.example.py config.py
```

2. Add your own site definitions in `config.py`  
3. Implement site logic in `sites/site_xxx.py`  
4. Run:
```bash
python main.py
```

---

## 中文说明

Invite Balance Collector 是一个基于 Playwright 的自动化框架，用于：
- 登录网站后台
- 抓取邀请 / 推广钱包余额
- 汇总写入 Excel

### 功能特点
- 插件式网站模块
- 浏览器自动化
- Excel 汇总
- 支持 Windows / Linux
- 可安全上传 GitHub（不包含隐私信息）

### 使用步骤
1. 复制配置模板：
```bash
cp config.example.py config.py
```

2. 在 `config.py` 中填写你自己的网站信息  
3. 在 `sites/` 目录实现对应抓取逻辑  
4. 运行：
```bash
python main.py
```

---

## Site Plugin Specification（插件规范）

Each site module must implement:

```python
def fetch(site: dict) -> float:
    '''
    site: configuration dict from config.py
    return: numeric balance
    '''
```

The module filename must match `site['module']`.
