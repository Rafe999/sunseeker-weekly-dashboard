# Sunseeker Weekly Dashboard

Sunseeker美国亚马逊站7月销售与广告可视化看板。

## 当前数据
- W1：2026-07-01 至 2026-07-07
- W2：2026-07-08 至 2026-07-14
- 产品线：V3、X5、S4、X3 Plus、X7

## 指标
Sales、Units、Daily Run Rate、Sessions、CVR、Ad Spend、Ad Sales、ACOS、TACOS、ASOAS，以及销量变化贡献拆解。

## GitHub Pages发布
仓库为Public，并从以下位置发布：

- Source：Deploy from a branch
- Branch：main
- Folder：/(root)

根目录的 `index.html` 会自动发布，不需要手动运行Workflow。

## 更新方式
看板当前为自包含静态页面。更新By Day数据后，替换 `index.html` 中的数据并推送到 `main`，Pages会自动刷新。

## Deployment trigger
Pages refresh triggered on 2026-07-22 after repository visibility and branch-source setup were confirmed.

## 差评洞察看板

Robot Lawn Mower 低星评论可视化已加入 [review-dashboard](./review-dashboard/)：支持 X3 Plus、S4、X7、X5 品线筛选，展示问题覆盖率、星级结构、产品风险矩阵以及 Current / Target / Gap / Action 行动方案。

- 在线地址：https://rafe999.github.io/sunseeker-weekly-dashboard/review-dashboard/
- 数据口径：30 行低星评论，按行统计且未去重；一条评论可命中多个问题类别。

## SC 仓储费 & 超龄附加费看板

SC Robot Mower 仓储成本可视化已加入 [storage-dashboard](./storage-dashboard/)：展示 By 月仓储费、By 月超龄附加费、By 品线成本结构、当前库龄风险、V3 移除回收期与清仓 Action Plan。

- 在线地址：https://rafe999.github.io/sunseeker-weekly-dashboard/storage-dashboard/
- 仓储费口径：Amazon 原生字段 `estimated_monthly_storage_fee`
- 数据范围：仓储费 Jan–Jun 2026；超龄附加费 Jan–Jul 2026
