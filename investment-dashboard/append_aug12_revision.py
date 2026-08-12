import json, pathlib
p=pathlib.Path('investment-dashboard/data/forecast.json')
f=json.loads(p.read_text(encoding='utf-8'))
rev={
  'asOf':'2026-08-12T23:36:00+08:00',
  'type':'aug12_official_cpi_postmortem',
  'preserveOriginalForecast':True,
  'summary':'8/12三只基金官方净值全部上涨，按截图反推份额计算合计实际盈利约189.75元；原始8/12基准路径同口径预计盈利约24.25元，方向正确但明显低估上涨幅度约165.50元。美国7月CPI随后公布：环比+0.1%、同比+3.4%，核心环比+0.2%、核心同比+2.5%，整体温和；美股科技/半导体同步走强，降低8/13宏观压制风险，但A股科技已先行大涨，需要防止高开后的获利回吐。',
  'evidence':[
    '025500：8/12官方净值1.6560，日涨2.33%，日净值变动+0.0377，按2018.0272份计算实际盈利约76.08元；原8/12预测日涨约0.22%，方向正确但显著低估。',
    '024481：8/12官方净值2.0046，日涨2.42%，日净值变动+0.0474，按1528.742份计算实际盈利约72.46元；原预测日涨约0.37%，方向正确但显著低估。',
    '024975：8/12官方净值2.5826，日涨1.97%，日净值变动+0.0498，按827.609份计算实际盈利约41.21元；原预测日涨约0.27%，方向正确但低估。',
    '近5个交易日累计（8/6、8/7、8/10、8/11、8/12）：025500约+5.53%，024481约+8.23%，024975约+8.59%。',
    '8/12养基宝17:33穿透估算+182.93元，最终官方实际约+189.75元，仅少估盈利约6.82元。',
    '美国7月CPI：headline环比+0.1%、同比+3.4%；core环比+0.2%、同比+2.5%。CPI后纳指与半导体板块走强，短端加息预期下降。'
  ],
  'modelAssessment':{
    'direction':'correct',
    'magnitude':'materially_underestimated',
    'predictedPnl':24.25,
    'actualPnl':189.75,
    'pnlError':165.50,
    'reason':'模型在8/11大跌后提高了均值回归权重，但对8/12 A股科技四条主线同步修复的共振强度估计不足；同时低估CPO/PCB、存储、半导体材料设备同日风险偏好恢复的幅度。'
  },
  'nextSessionProbability':{
    'date':'2026-08-13',
    '025500':{'up':45,'sideways':35,'down':20},
    '024481':{'up':52,'sideways':31,'down':17},
    '024975':{'up':48,'sideways':33,'down':19},
    'portfolio':{'up':49,'sideways':33,'down':18}
  },
  'forward5DayProbability':{
    'window':'2026-08-13/2026-08-19',
    'portfolio':{'up':50,'sideways':28,'down':22},
    'bullTrigger':'CPI后的美债短端不再上冲、SOX/纳指维持强势，且A股CPO/PCB与半导体设备材料至少两条主线连续两日放量不破位。',
    'sidewaysTrigger':'美股科技维持强势但A股8/12先行上涨后出现高位轮动，成交保持但无持续增量。',
    'bearTrigger':'10年美债重新上冲至4.75%以上、油价再度急升或A股科技高开低走并跌破8/12收盘结构。'
  },
  'actions':{
    '025500':'CPI温和且美股存储/半导体偏强，8/13可以从“完全观望”升为“回踩确认后小额加仓候选”，不追高开。',
    '024481':'当前优先级最高；CPO/PCB 8/12同步强，若8/13不出现高开低走，可作为第一笔小额加仓首选。',
    '024975':'继续核心持有；8/12修复后叠加CPI利好，但近5日已涨约8.6%，只在回踩承接良好时加，不追涨。'
  },
  'portfolioView':'CPI结果对科技是边际利好，8/13由“等待事件”切换为“允许条件式小额加仓”。但8/12 A股科技已先行上涨，最优策略不是开盘追涨，而是观察高开后的承接；024481优先，024975次之，025500再次。'
}
revs=f.setdefault('revisions',[])
if not any(x.get('type')=='aug12_official_cpi_postmortem' for x in revs):
    revs.append(rev)
p.write_text(json.dumps(f,ensure_ascii=False,indent=2),encoding='utf-8')
