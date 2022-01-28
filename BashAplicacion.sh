// Esto se puede crear en un CodeBuild

aws lambda create-function --function-name payclip --zip-file fileb://Aplicacion.zip --handler index.handler --runtime Python3.8