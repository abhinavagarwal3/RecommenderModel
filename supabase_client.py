import os

from supabase import create_client

# Load environment variables from .env file
SUPABASE_URL = "https://mxoxsbwxtjgtatnnslrm.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14b3hzYnd4dGpndGF0bm5zbHJtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE1ODQ2MDcsImV4cCI6MjA0NzE2MDYwN30.RPULjBmBswci6vwuMrtowv8E4CdOQD_ciO2D4RSw4F0"

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
