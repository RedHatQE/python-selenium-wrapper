### Running nosetests with the screenshots plugin
* `nosetests --with-webuiscreenshots`
* by default, a `Screenshots` directory is created
* screenshots are organized as follows
  * `Screenshots`
    * `<run date #1>`
      * `<test case name #1>`
        * `<screenshot date #1>.png`
        * `<screenshot date #2>.png`
        * `<screenshot date #k>.png`
      * `<test case name #2>`
      * `<test case name #l>`
    * `<run date #2>`
    * `<run date #m>`
* passing screenshots are removed unless `--keep-passing-screenshots` swithc is specified
      
