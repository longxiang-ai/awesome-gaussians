# 搜索配置文件使用指南

## 概述

ArXiv 爬虫现在支持通过配置文件来自定义搜索查询。用户只需要在 `data/search_config.json` 文件中定义关键词，爬虫会自动生成相应的 arXiv 搜索查询。

## 配置文件格式

配置文件位置：`data/search_config.json`

```json
{
  "search_config": {
    "description": "arXiv搜索配置 - 定义在摘要和/或题目中搜索的关键词",
    "both_abstract_and_title": [
      "gaussian splatting",
      "3d gaussian",
      "gaussian splat",
      "3dgs",
      "4d gaussian"
    ],
    "abstract_only": [
      "neural radiance field gaussian",
      "volumetric rendering gaussian",
      "point cloud gaussian"
    ],
    "title_only": [
      "3D scene reconstruction",
      "neural rendering"
    ]
  }
}
```

## 配置选项说明

### `both_abstract_and_title`
- **功能**：这些关键词将同时在论文摘要(abstract)和题目(title)中搜索
- **生成查询**：每个关键词会生成两个搜索条件：`abs:"keyword"` 和 `ti:"keyword"`
- **适用场景**：核心关键词，希望在摘要或题目中任一位置出现

### `abstract_only`
- **功能**：这些关键词只在论文摘要(abstract)中搜索
- **生成查询**：每个关键词生成：`abs:"keyword"`
- **适用场景**：技术细节关键词，通常在摘要中描述但不会出现在题目中

### `title_only`
- **功能**：这些关键词只在论文题目(title)中搜索
- **生成查询**：每个关键词生成：`ti:"keyword"`
- **适用场景**：主题关键词，希望论文明确以此为主题

## 使用示例

### 示例1：基础配置
如果你只关心 Gaussian Splatting 相关论文：

```json
{
  "search_config": {
    "both_abstract_and_title": [
      "gaussian splatting",
      "3dgs"
    ],
    "abstract_only": [],
    "title_only": []
  }
}
```

生成的查询：`(abs:"gaussian splatting" OR ti:"gaussian splatting" OR abs:"3dgs" OR ti:"3dgs")`

### 示例2：扩展配置
如果你想搜索更广泛的神经渲染论文：

```json
{
  "search_config": {
    "both_abstract_and_title": [
      "gaussian splatting",
      "neural radiance field",
      "nerf"
    ],
    "abstract_only": [
      "volumetric rendering",
      "differentiable rendering"
    ],
    "title_only": [
      "3D reconstruction",
      "novel view synthesis"
    ]
  }
}
```

## 注意事项

1. **关键词区分大小写**：arXiv 搜索是区分大小写的，建议使用小写
2. **特殊字符**：如果关键词包含引号或特殊字符，请确保 JSON 格式正确
3. **搜索范围**：添加太多关键词可能会增加搜索时间和结果数量
4. **默认后备**：如果配置文件不存在或格式错误，系统会使用默认的 Gaussian Splatting 搜索查询

## 配置文件验证

运行爬虫时，日志会显示生成的搜索查询，例如：

```
INFO - Generated search query from config: (abs:"gaussian splatting" OR ti:"gaussian splatting" OR ...)
```

## 修改配置后的使用

1. 编辑 `data/search_config.json` 文件
2. 运行爬虫：`python scripts/arxiv_crawler.py`
3. 查看日志确认查询是否正确生成

## 故障排除

- **配置文件不存在**：系统会自动使用默认查询并记录警告
- **JSON 格式错误**：检查 JSON 语法，确保引号和逗号正确
- **搜索结果为空**：可能关键词过于具体，尝试添加更通用的关键词 