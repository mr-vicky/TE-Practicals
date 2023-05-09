<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Employees</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            <!-- background-color: #f2f2f2; -->
            background-color:#9fd0bc;
            color:white
          }
          h1 {
            text-align: center;
            color: black;
            margin-top: 50px;
          }
          
          table {
            border-collapse: collapse;
            width: 80%;
            margin: 50px auto;
            box-shadow: 0px 0px 10px #ddd;
            border-radius: 10px;
            overflow: hidden;
            background-color: black;
            color:white
          }
          name, title, department, salary{
            color:white;
          }
          th, td {
            text-align: left;
            padding: 10px;
            border: 1px solid #ddd;
            color:white;
            background-color: green;
          }
          th {
            background-color: #105610;
            color: white;
          }
          tr:hover {
            <!-- background-color: #f5f5f5; -->
            background-color:gray;
            color:white;
          }
        </style>
      </head>
      <body>
        <h1>Employee Data</h1>
        <table>
          <tr>
            <th>Name</th>
            <th>Title</th>
            <th>Department</th>
            <th>Salary</th>
          </tr>
          <xsl:for-each select="employees/employee">
            <tr>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="department"/></td>
              <td><xsl:value-of select="salary"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>