import sqlparse

sql = 'SELECT * FROM users WHERE age > 20'
parsed = sqlparse.parse(sql)

# 输出解析后的SQL语句，它是一个列表，每个元素都是一个Token对象
print(parsed)


# 输出结果如下：
#
# ```
# [<Select 'SELECT * FROM users WHERE age > 20'>]
# ```

# 解析后的SQL语句是一个列表，每个元素都是一个Token对象。你可以使用Token对象的方法来获取更多信息，例如：
#
# ```
# 获取SQL语句的类型
print(parsed[0].get_type())
# 输出：'SELECT'

# 获取SQL语句的表名
print(parsed[0].get_identifiers())
# 输出：['users']

# 获取SQL语句的查询字段
#print(parsed[0].get_field_list())  # 输出：['*']

# 获取SQL语句的WHERE子句
print(parsed[0].get_where())  # 输出：'WHERE age > 20'
# ```
#
# 请注意，以上代码仅作为示例，不能直接运行。你需要根据实际情况自行修改代码。
#
# 此外，你也可以使用Python标准库中的其他模块来解析SQL语句，例如pyparsing模