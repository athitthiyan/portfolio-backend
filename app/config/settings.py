import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:Athitthiyan%40@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require"
)