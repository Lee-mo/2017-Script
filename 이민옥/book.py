from urllib import request, parse

url = 'http://openapi.animal.go.kr:80/openapi/service/rest/abandonmentPublicSrvc?_wadl&type=xml'
queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : 'OyfS4qqxnYyHXNdGgHg%2Bem2F%2FLAjaG4C0X2kgqycc%2B2G3%2F0flCjg9GIptnv23C3UXWRH3wjd3EuE31%2FGSX71ZA%3D%3D',
                                      parse.quote_plus('bgnde') : '20140601',
                                parse.quote_plus('endde') : '20140630', parse.quote_plus('upkind') : '417000', parse.quote_plus('kind') : '',
                                parse.quote_plus('upr_cd') : '', parse.quote_plus('org_cd') : '', parse.quote_plus('care_reg_no') : '',
                                parse.quote_plus('state') : 'notice', parse.quote_plus('pageNo') : '1', parse.quote_plus('numOfRows') : '10' })
request1 = request.Request(url+queryParams)
request1.get_method = lambda: 'GET'
response_body = request.urlopen(request1).read()
print(response_body)
