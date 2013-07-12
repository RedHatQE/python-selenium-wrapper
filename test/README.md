### Running nosetests with the screenshots plugin
* `nosetests --with-webuiscreenshots`
* by default, a `Screenshots` directory is created
* passing screenshots are removed unless `--keep-passing-screenshots` switch is specified

#### screenshots are organized as follows
```
Screenshots/
  run_date_#1/
    [FAILED_|ERROR_]test_case_id_#1/
      screenshot_date_#1.png
      screenshot_date_#2.png
      screenshot_date_#k.png
    test_case_id_#2/
    test_case_id_#l/
  run_date_#2/
  run_date_#m/
```


      
