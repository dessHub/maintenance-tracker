
class Config(object):
	"""
	Common configurations
	"""

	DEBUG = True

class DevelopmentConfig(Config):
	"""
	Development configurations
	"""

	DEBUG = True
	SECRET_KEY = "itsasecret"

class ProductionConfig(Config):
	"""
	Production configurations
	"""
	DEBUG = False
	TESTING = False
	SECRET_KEY = "itsasecret"

class TestingConfig(Config):
	"""
	Testing configurations
	"""

	TESTING = True
	SECRET_KEY = "itsasecret"

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
