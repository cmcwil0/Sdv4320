import pygal

def bar_graph(stock, start_date, end_date, open, high, low, close):
    graph = pygal.Bar()
    graph.title = f'Stock Data for {stock}: {start_date} to {end_date}'
    graph.x_labels = map(str, range(start_date, end_date))
    graph.add('Open', open)
    graph.add('High', high)
    graph.add('Low', low)
    graph.add('Close', close)
    graph.render_in_browser()


def line_graph(stock, start_date, end_date, open, high, low, close):
    graph = pygal.Line()
    graph.title = f'Stock Data for {stock}: {start_date} to {end_date}'
    graph.x_labels = map(str, range(start_date, end_date))
    graph.add('Open', open)
    graph.add('High', high)
    graph.add('Low', low)
    graph.add('Close', close)
    graph.render_in_browser()