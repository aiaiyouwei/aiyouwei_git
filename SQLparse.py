
import sqlparse
#sql简单sql
sql = r"""SELECT CUST_ID,CUST_NAME from PDATA.T03_DEPOSIT_ACCT_INFO WHERE DATA_DT='$bizDate$' """

s1 = sqlparse.parse(sql)
print(s1)
#reindent 格式化  keywork_case 关键字变大写
s2 = sqlparse.format(sql,reindent=True,keyword_case='upper')
print(s2)
s3 = s1[0].tokens
print(s3)