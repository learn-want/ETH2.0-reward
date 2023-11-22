import plotly.graph_objects as go
import plotly.io as pio

uzh_colors = {'blue': '#0028a5', 'blue_80': '#3353b7', 'blue_60': '#667ec9', 'blue_40': '#99a9db', 'blue_20': '#ccd4ed',
              'red': '#dc6027', 'red_80': '#e38052', 'red_60': '#eaa07d', 'red_40': '#f1bfa9', 'red_20': '#f8dfd4',
              'green': '#91c34a', 'green_80': '#aad470', 'green_60': '#bfdf94', 'green_40': '#d5e9b7', 'green_20': '#eaf4db',
              'yellow': '#fede00', 'yellow_80': '#fbe651', 'yellow_60': '#fcec7c', 'yellow_40': '#fdf3a8', 'yellow_20': '#fef9d3',
              'grey': '#a3adb7', 'grey_80': '#b5bdc5', 'grey_60': '#c8ced4', 'grey_40': '#dadee2', 'grey_20': '#edeff1',
              'turquoise': '#0b82a0', 'turquoise_80': '#3c9fb6', 'turquoise_60': '#6bb7c7', 'turquoise_40': '#9ed0d9', 'turquoise_20': '#cfe8ec',
              'green2': '#2a7f62', 'green2_80': '#569d85', 'green2_60': '#80b6a4', 'green2_40': '#abcec2', 'green2_20': '#d5e7e1'}

uzh_color_map = ['#0028a5', '#dc6027', '#91c34a', '#fede00', '#a3adb7', '#0b82a0', '#2a7f62',  # FULL
                 '#667ec9', '#eaa07d', '#bfdf94', '#fcec7c', '#c8ced4', '#6bb7c7', '#80b6a4',  # 60%
                 '#3353b7', '#e38052', '#aad470', '#fbe651', '#b5bdc5', '#3c9fb6', '#569d85',  # 80%
                 '#99a9db', '#f1bfa9', '#d5e9b7', '#fdf3a8', '#dadee2', '#9ed0d9', '#abcec2',  # 40%
                 '#ccd4ed', '#f8dfd4', '#eaf4db', '#fef9d3', '#edeff1', '#cfe8ec', '#d5e7e1']  # 20%

# 创建绘图模板
template = go.layout.Template()
template.layout.colorway = uzh_color_map
template.layout.font.family = 'TheSans'
template.layout.font.size = 12+6
template.layout.title.font.family = 'TheSans'
template.layout.title.font.size = 16+4
template.layout.paper_bgcolor = 'rgba(0,0,0,0)'
template.layout.plot_bgcolor = 'rgba(0,0,0,0)'
template.layout.xaxis.title.font.family = 'TheSans'
template.layout.xaxis.title.font.size = 16+4
template.layout.xaxis.linecolor = '#000'
template.layout.xaxis.linewidth = 1.2+0.3
template.layout.yaxis.title.font.family = 'TheSans'
template.layout.yaxis.title.font.size = 16+4
template.layout.yaxis.linecolor = '#000'
template.layout.yaxis.linewidth = 1.2+0.3
# template.layout.yaxis.mirror = True
# template.layout.xaxis.mirror = True

# 应用绘图模板
# go.Figure().update_layout(template=template)
pio.templates["uzh_plotly"] = template
pio.templates.default = "simple_white+uzh_plotly"

