class Settings:
    # Google API
    GOOGLE_API_KEY = ''    

    # Postgres DB
    POSTGRES_USER = 'interpreter'
    POSTGRES_PASSWORD = 'passw0rd'
    POSTGRES_DB = 'interpretationsdb'
    POSTGRES_HOST = '192.168.122.254' # NOTE: localhost wasn't working for some reason, therefore using my local vm local ip addr
    POSTGRES_PORT = '5432'
