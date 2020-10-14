[business]
pip
    pip3 install requests

[maintenance][development]
pip3 install flask
# flask run
export FLASK_ENV=development
flask run -h 0.0.0.0

[execute]
nohup python3 -u /root/python/paloalto_add_address/business.py > /dev/null &

[maintenance][product]
# install
pip install gunicorn
# start
gunicorn -c gunicorn_config.py -D flask_main:app
# shutdown
pstree -p | grep gunicorn
kill -9 pid

[credential]
172.16.31.87
root
Gq34Ko90#110

[todo]
add local app authentication
add email function

[paloauto]
delete address: the address of address group (or the policy) must be set dynamic, the address can be deleted 

[oauth2 sso]
first handshake
request
    browser or program -> http://192.168.2.110:5000/->http://172.30.2.115:8080/oa/oauth2.action?client_id=pa&response_type=code&redirect_uri=192.168.2.110:5000/login
response
    unauth: return unauthenticated page
    success: second handshake

second handshake
Auto
request
    browser -> http://172.30.2.115:8080/2.0/oauth2LoginAuto.action
response
    unauth: return unauthenticated page
    manual Login: return oauth2Login.jsp
    success LoginAuto: return http://192.168.2.110:5000/login?code=xxxx

Manual
request
    browser -> http://172.30.2.115:8080/2.0/oauth2Login.action
response
    unauth: return unauthenticated page
    manual Login: return oauth2Login.jsp
    success LoginAuto: return http://192.168.2.110:5000/login?code=xxxx

three handshake
request
    requests(program) -> http://172.30.2.115:8080/oa/oauth2/json/getToken.action
                POST
                Header: Content-Type': 'application/x-www-form-urlencoded'
                data: code:xxxx
response
    success: {"username":"david.wei","token":"ttt"}
    failure: {}


    
    


