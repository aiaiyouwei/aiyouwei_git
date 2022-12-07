import sqlparse
# import token
# SQL解析主要包含：词法分析、语义语法分析、优化和执行代码生成
    # SQL解析由词法分析和语法、语义分析两个部分组成。词法分析主要是把输入转化成若干个Token，其中Token包含key和非key
    # 语法分析是生成语法树的过程，这是整个解析过程中最核心、最复杂的环节
# 初始化代码方法有四种：parse，parsestream，format，split
sql = r"""SELECT CUST_ID,CUST_NAME FROM PDATA.T03_DEPOSIT_ACCT_INFO WHERE DATA_DT='$BIZDATA$' """
#parse 返回一个 sqlparse.sql.Statement的元组，我们可以递归方式获得输出。
n=0
for each in sqlparse.parse(sqlparse.format(sql,reindent=True,keyword_case='upper')):
    n+=1
    print(each,n)
#调用了parsestream来完成流式解析
'''
format()函数接受关键字参数:
    keyword_case 关键词 upper、lower sql的保留字大小写
    identifier_case 标识符的upper、lower大小写
    strip_comments=Ture删除注释
    reindent=Ture美化sql缩进语句发生改变
'''

parsed = sqlparse.parse(sql)
stmt = parsed[0]
sql_tokens=stmt.tokens
for each_token in sql_tokens:
    if str(each_token.ttype) == 'Token.Text.Whitespace' or str(each_token.ttype) == 'Token.Text.Whitespace.Newline':
        continue
    else:
        print("\n类型：")
        print(each_token.ttype)
        print(type(each_token))

        print("\n内容："+each_token.value)
        print(type(each_token))
'''
# ===================Special token types===================  特殊类型
Text = Token.Text
Whitespace = Text.Whitespace
Newline = Whitespace.Newline
Error = Token.Error

# ===================Text that doesn't belong to this lexer (e.g. HTML in PHP)===================  不属于此lexer的文本（例如PHP中的HTML）
Other = Token.Other
 
# ===================Common token types for source code=================== 源代码的通用类型
Keyword = Token.Keyword
Name = Token.Name
Literal = Token.Literal
String = Literal.String
Number = Literal.Number
Punctuation = Token.Punctuation
Operator = Token.Operator
Comparison = Operator.Comparison
Wildcard = Token.Wildcard
Comment = Token.Comment
Assignment = Token.Assignment
 
# ===================Generic types for non-source code=================== 非源代码的泛型类型 注释
Generic = Token.Generic
Command = Generic.Command
 
# ===================String and some others are not direct children of Token.=================== 字符串和其他一些不是Token的直接子级。
# alias them:
Token.Token = Token
Token.String = String
Token.Number = Number
 
# ===================SQL specific tokens===================SQL类型
DML = Keyword.DML
DDL = Keyword.DDL
CTE = Keyword.CTE
'''
#flatten()  用于解析子组