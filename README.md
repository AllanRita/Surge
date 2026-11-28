# Surge 规则库

## V2.0 维护方式

每天计划于北京时间 11:17 从 blackmatrix7 的 `rule/Surge` 同步全部 `.list` 文件，也可手动运行。同步保留上游相对路径、规则顺序和不同解析格式，并应用已登记的排除项。[上游来源](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Surge) · [同步后的规则](Rule/Upstream/)

工作流校验全部规则文件，用 OpenPhish 核对精确的 `DOMAIN` 规则。新命中会记录文件、行号和主机名，供复核。已登记的删除记录在后续同步中继续生效。[最新发布报告](Rule/Upstream/SECURITY-SYNC-REPORT.json)

每次运行的摘要列出各步骤结果。同步或发布失败时，请先查看该次运行的摘要和日志。仓库中的报告对应最近一次成功发布。[运行记录](../../actions/workflows/batch-preflight.yml) · [项目交接记录](SURGE-PROJECT-STATE.md)

个人补充规则位于 `Rule/Personal/`。此仓库公开，该目录的内容也公开可读。同步会校验个人规则保持原样。Surge 主配置和策略顺序由用户单独维护。
