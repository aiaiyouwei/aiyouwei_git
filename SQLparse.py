
import sqlparse


if __name__ == '__main__':
    try:
        # sql简单sql
        sql = r"""SELECT CUST_ID,CUST_NAME from PDATA.T03_DEPOSIT_ACCT_INFO WHERE DATA_DT='$bizDate$' """
        s1 = sqlparse.parse(sql)
        print(s1)
        # reindent 格式化  keywork_case 关键字变大写
        s2 = sqlparse.format(sql, reindent=True, keyword_case='upper')
        print(s2)
        s3 = s1[0].tokens
        print(s3)
        for tokend in s3:
            print(tokend.ttype, tokend.value)

        #s4 = s1[0]._pprint_tree()
        print("~~~~~~~~~~~~~~~~~")
        #print(s4)
        #s5 = sqlparse.sql.Where(tokend)
        s6 = s1[0].get_type()

        #print(s5)
        #print(s6)
        s7 = sqlparse.sql.Where(s1[0])

        print(s7)

    except Exception as e :
        print("出错了")
        print(e)

