

import easyquotation

quotation = easyquotation.use('sina')

quotation.market_snapshot(prefix=True)

quotation.stocks(['000001', '162411'])

quotation.stocks(['sh000001', 'sz000001'], prefix=True)

