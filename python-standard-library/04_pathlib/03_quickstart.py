# 创建一个支持三种hash算法的context对象
from passlib.context import CryptContext

# myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])

# 这将加载 schemes 列表中的第一个算法 （sha256_crypt），
# 生成一个新的 salt，并对密码进行哈希处理：
# hash1 = myctx.hash("joshua")
# print(hash1)

# 验证密码时，算法会自动识别：
# result1 = myctx.verify("gtnw", hash1)
# result2 = myctx.verify("joshua", hash1)
# print(f"result1: {result1}")
# print(f"result2: {result2}")

# 或者，你可以显式地选择一种配置的算法，在实践中很少需要：
# hash2 = myctx.hash("dogsnamehere", scheme="md5_crypt")
# print(f"hash2: {hash2}")
#
# result3 = myctx.verify("letmein", hash2)
# result4 = myctx.verify("dogsnamehere", hash2)
#
# print(f"result3: {result3}")
# print(f"result4: {result4}")


# 如果没有另有说明，则 context 对象将在创建新哈希时使用 schemes 中列出的第一个算法。可以使用 default 关键字更改此默认值：
myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"],
                     default="des_crypt")
hash5 = myctx.hash("password")
print(f"hash5: {hash5}")

print(myctx.identify(hash5))