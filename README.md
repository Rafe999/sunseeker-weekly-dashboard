# Sunseeker Weekly Dashboard

Sunseeker美国亚马逊站7月销售与广告可视化看板。

## 当前数据
- W1：2026-07-01 至 2026-07-07
- W2：2026-07-08 至 2026-07-14
- 产品线：V3、X5、S4、X3 Plus、X7

## 指标
Sales、Units、Daily Run Rate、Sessions、CVR、Ad Spend、Ad Sales、ACOS、TACOS、ASOAS，以及销量变化贡献拆解。

## GitHub Pages发布
仓库改为Public后，在 `Settings → Pages` 中选择：

- Source：Deploy from a branch
- Branch：main
- Folder：/(root)

保存后，根目录的 `index.html` 会自动发布，不需要手动运行Workflow。

## 更新方式
看板当前为自包含静态页面。更新By Day数据后，替换 `index.html` 中的数据并推送到 `main`，Pages会自动刷新。
