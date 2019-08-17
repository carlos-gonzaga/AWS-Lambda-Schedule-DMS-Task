# AWS-Lambda-Schedule-DMS-Task

Cria um agendamento do Cloudwatch, o qual chama o Lambda passando a ARN da Migration Task existente no DMS.

O Lambda inicia a task, ou as tasks, de acordo com as ARNs recebidas.
