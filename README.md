# Example

Here's how you run it:
```
$ python3 templater.py 
[{'data_desc': ' R-foreign description', 'data_title': ' R-foreign TITLE'},
 {'data_desc': ' R-Basic description', 'data_title': ' R-Basic TITLE'}]
```

Here's what it produces:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Bundles in Clear Linux OS for Intel® Architecture</title>
    <style type="text/css">
    </style>
  </head>
  <body>
    <table>
      <thead>
          <tr>
              <th align=left>Bundle Name</th>
              <th align=left>Description</th>
          </tr>
      </thead>

        <tbody>
          <tr>
            <td class="bundlename"> R-foreign TITLE</td>
            <td class="bundledesc"> R-foreign description</td>
          </tr>
        </tbody>

        <tbody>
          <tr>
            <td class="bundlename"> R-Basic TITLE</td>
            <td class="bundledesc"> R-Basic description</td>
          </tr>
        </tbody>

    </table>
  </body>
 </html>
 ```