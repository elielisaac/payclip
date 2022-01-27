import json
import pymysql.cursors


def lambda_handler(event, context):
    connection = pymysql.connect(host='', user='', password='', database='', cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            try:
                cp = json.loads(event['body'])['cp']
                sql = "SELECT `name`, `owner`, `specie` FROM `pet`"
                cursor.execute(sql, (cp,))
                result = cursor.fetchone()
                result['name'] = result.pop('name')
                result['owner'] = result.pop('owner')
                result['specie'] = result.pop('specie')


                connection.commit()
                return {
                    'statusCode': 200,
                    'headers': {
                        "Access-Control-Allow-Headers" : "Content-Type",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Credentials": "true",
                        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                    },
                    'body': json.dumps({
                        'success': True,
                        'data': result})
                }
            except Exception as e:
                return {
                    'statusCode': 400,
                    'headers': {
                        "Access-Control-Allow-Headers" : "Content-Type",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Credentials": "true",
                        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                        },
                    'body': json.dumps({
                        'success': False,
                        'data': {}})
                }

            