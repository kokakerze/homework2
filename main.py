from urllib.parse import urlparse, ParseResult


def parse(query: str) -> dict:
    t=urlparse(query)
    result = {}
    if t[4]!="":
        data=t[4]
        datalist=data.split("&")


        for i in range (len(datalist)):
            if datalist[i]!="":
                element=str(datalist[i]).split("=")
                result[element[0]] = element [1]
        return result
    else:
        return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:

    result = {}
    if query != "":
        datalist = query.split(";")
        for i in range(len(datalist)):
            if datalist[i] != "":
                element = str(datalist[i]).split("=", 1)
                result[element[0]] = element[1]
        return result
    else:
        return result



if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}


