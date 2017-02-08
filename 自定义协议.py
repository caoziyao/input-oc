
Reset
	类型  Reset 
	
配置
	类型 DATA

配置完成
	类型 FLAT(SUCCESS, FAILURE)
	
请求
	类型 	W/R		Addr		Rem			TimeOut		DATA
			读写	节点地址	目的地址	超时时间
应答
	类型 	W/R		Addr		Rem			ERR			DATA
			读写	节点地址	目的地址	错误码

状态上报
	类型	
	
	
login 请求
	form = {
		'cmd': 'login',
		'addr': ID,
		'timeout': 0,
		'password': bbq_passwd
	}
login 应答
	form = {
		'cmd': 'login',
		'err': True/False
	}