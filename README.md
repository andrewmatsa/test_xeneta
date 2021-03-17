![](https://www.xeneta.com/hubfs/Product%20Section%20%284%29.png)
### Xeneta automation test framework
----
According to requirements https://github.com/xeneta/test-automation-task implemented test framework. It shows correct structure and approach and possibility of enhancement.

### Test Cases
----
|Demo page|
| --------- | 
| **Verify header footer menus on page**  | 
| Verify banner section is displayed with text inside| 
| Verify services center block| 
| Verify footer menu with links| 
| Verify careers page has header menu bar| 
| Verify banner section is displayed with text inside| 
| Verify part of the team block| 
| Verify “What we do” block| 
| **Verify “Our values” block with switchers**| 
| Verify “Global Tribe” block with links below| 
| **Verify “Open roles” with dropdowns and text inside**| 
| Verify footer menu with links| 
Several verifications were implemented. Detailed Test steps is implemented in doc stings for each test. example

> Note: selected 


```javascript
  def test_001_verify_services(self):
  	"""
  	DESCRIPTION: Verify services block is displayed
  	EXPECTED: Watch videos, Book a meeting, Group live demo is displayed
  	"""
```


### Instruction to install
----
1. Python>3 https://www.python.org/
2. Install and activate Virtual Environment https://docs.python.org/3/tutorial/venv.html
`$ python3 -m venv env`
3. Install dependencies
`$ pip install -r requirements.txt`
4. Download chrome driver https://chromedriver.chromium.org/
5. Move downloaded "chromedriver" to Virtual Env (Step2) to ./bin/ folder
6. run test(s)
open console and run one of the following command https://docs.pytest.org/en/stable/usage.html
`$ pytest` run all tests
`$pytest -m careers` run tests with mark "careers"
