# sasonline_python_auth
This script can help people trying to connect sasonline Api and generate a bearer token using https://alphaapi.sasonline.in. Using the bearer token one can  connect the API.

**How to make use of this:
**
1. Add client-secret(share by sasonline support team) to config.py
2. Run the auth_generate_response.py it will open the browser with the login uri , just input the username, password + totp. if the credentials correct it will be redirected to redirect_uri  mentioned in the config. 
3. Just copy the browser redirected URL and paste it to auth_generateBtoken.py authorization_response variable. 
4. Now run the auth_generateBtoken.py it can output the token


ref:
https://docs.authlib.org/en/latest/client/oauth2.html
https://drive.google.com/file/d/15HMf1ieewe2FgHxZJ-YIGeDtyNVEgCQ2/view
