import json
import pandas as pd
import duckdb

def lambda_handler(event, context):
    pandas_code = event.get('pandas_code')
    
    if not pandas_code:
        return {
            'statusCode': 400,
            'body': json.dumps('No Pandas code provided.')
        }
    
    try:
        exec(pandas_code, {"pd": pd, "duckdb": duckdb}, {})
        result = local_env.get('result', 'No result variable found.')
        
        return {
            'statusCode': 200,
            'body': json.dumps(str(result))
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error executing code: {str(e)}')
        }
