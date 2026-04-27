browsername="chrome"

match(browsername):

    case "chrome":
        print('open the chrome browser')
    
    case "firefox":
        print('open the firefox browser')
    
    case "edge":
        print('open the edge browser')

    case "webkit":
        print('open the webkit browser')

    case _:
        print('Given browser is wrong')

