#md5_test.py
import hashlib
#因为 MD5 算法是不可逆向的，所以，当服务器接收到请求后，同样需要对“@admin123”进行 MD5 加 密，然后，比对与调用者传来的 sign 加密串是否一致，从而来鉴别调用者是否有权限方位该接口
md5 = hashlib.md5()
sign_str = "@admin123"
sign_bytes_utf8 = sign_str.encode(encoding = "utf-8")
md5.update(sign_bytes_utf8)
#生成16进制的md5
sign_md5 = md5.hexdigest()
print(sign_md5)


#接口全参数加密防篡改
#不过，接口全参数的加密签名也存在弊端，因为 MD5 加密是不可逆的，所以，服务器端必须已知客户 端的接口参数和值，否则签名的验证就会失败。但一般接口在设计时对客户端所请求的参数并不完全已知， 例如，嘉宾手机号查询，服务器并不知道客户传的手机号具体是什么，只是通过数据库来查询该号码是否存 在。

