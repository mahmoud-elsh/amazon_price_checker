Simple web scrapping application that checks the price of an Amazon product and notifies the user if the price drops below a certain number.

How to use:

1.) Install packages: requests, plyer and bs4.

2.) Change link variable on line 11 to preferred product link.

3.) Change "User-Agent" key in the headers dictionary on line 15 to your own user-agent (Can be found on https://www.whatismybrowser.com/detect/what-is-my-user-agent/).

4.) Change price threshold on line 63 to preferred number (must be a str).
