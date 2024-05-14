import json
import threading
import logging
import uvicorn
from fastapi import FastAPI, Request

from prometheus_abnormal_metric import fetch_prometheus_metrics

app = FastAPI()

@app.get('/test')
async def test():
    return {
        "code": 0,
        "msg": "success",
        "data": "prometheus service is running"
    }

@app.post('/alert')
async def alert(request: Request):
    """
    return add alert
    :return:
    """
    args = await request.json()
    # 将obj写入文件中
    with open("alert_history.txt", "a") as f:
        f.write(json.dumps(args) + "\n")

    try:
        if args["status"] == "resolved":
        # 开启异步线程，获取异常时间内的prometheus指标，并保存到新文件中，文件名为时间戳
            thread = threading.Thread(target=fetch_prometheus_metrics, args=(args, ))
            thread.start()
    except Exception as e:
        logging.error(e)

    # from datetime import datetime
    # from prometheus_abnormal_metric import obtain_exceptions_in_times
    # alerts = args.get("alerts", [])

    # for alert in alerts:
    #     # 获取alert的startsAt属性，并将其转换为UTC时间格式
    #     alert_time = alert.get("startsAt")
    #     alert_time = alert_time[:-4] + "Z"

    #     start_time = (
    #         datetime.strptime(alert_time, "%Y-%m-%dT%H:%M:%S.Z").timestamp() - 60 * 5
    #     )
    #     end_time = datetime.strptime(alert_time, "%Y-%m-%dT%H:%M:%S.Z").timestamp() + 60

    #     # 调用obtain_exceptions_in_times函数获取在指定时间范围内的异常，并返回结果
    #     exceptions = obtain_exceptions_in_times(start_time, end_time)

    #     # 将获取到的异常结果赋值给alert字典中的exceptions键
    #     alert["exceptions"] = exceptions

    # args.update({"alerts": alerts})
    # MetaAgentvere_URL = "http://configuration_expert"
    # import logging, requests

    # logging.basicConfig(
    #     level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    # )

    # logging.debug("before launch goal")
    # # 将获取到的数据发送到MetaAgentvere，启动一个任务
    # requests.post(
    #     MetaAgentvere_URL + ":5050/launch_goal",
    #     json={
    #         "goal": "Here is the anomaly detection result. You should discuss and come up with a plan with detailed anaylsis based on the information. Here is the information: "
    #         + str(args),
    #         "team_up_depth": 1,  # the depth limit of nested teaming up
    #     },
    # )
    # logging.debug("after launch goal")
    return {
        "code": 0,
        "msg": "success",
        "data": ""
    }

if __name__ == "__main__":
    uvicorn.run(
        app = app,
        host = "0.0.0.0",
        port = 8023
    )



# {'receiver': 'db-gpt', 'status': 'firing', 'alerts': [{'status': 'firing', 'labels': {'alertname': 'NodeMemSwapped', 'category': 'node', 'instance': 'node_exporter:9100', 'job': 'node_exporter', 'level': '2', 'severity': 'INFO'}, 'annotations': {'description': 'node:ins:swap_usage[ins=] = 0.71 > 1%\n', 'summary': 'INFO NodeMemSwapped @node_exporter:9100 0.71'}, 'startsAt': '2024-04-07T11:41:10.038Z', 'endsAt': '0001-01-01T00:00:00Z', 'generatorURL': 'http://67463bce7537:9090/graph?g0.expr=node%3Ains%3Aswap_usage+%3E+0.01&g0.tab=1', 'fingerprint': '624e683c4c74cd4e', 'exceptions': {'cpu': {'node_entropy_available_bits': [256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0, 256.0], 'node_load5': [1.33, 1.46, 2.51, 2.51, 2.75, 2.75, 3.44, 3.51, 3.51, 3.52, 3.52, 3.6, 3.74, 3.74, 4.4, 4.4, 4.66, 4.62, 4.62, 4.67, 4.67, 4.6, 4.57, 4.57, 4.49, 4.49, 4.44, 4.36, 4.36, 4.29, 4.29, 4.22, 4.15, 4.15, 4.08, 4.08, 4.03, 3.96, 3.96, 3.89, 3.89, 3.83, 3.88, 3.88, 3.82, 3.82, 3.75, 3.71, 3.71, 3.65, 3.65, 3.59, 3.56, 3.56, 3.53, 3.53, 3.47, 3.42, 3.42, 3.38, 3.38, 3.32, 3.3, 3.3, 3.24, 3.24, 3.19, 3.13, 3.13, 3.08, 3.08, 3.03, 3.0, 3.0, 2.95, 2.95, 2.9, 2.85, 2.85, 2.8, 2.8, 2.77, 2.73, 2.73, 2.73, 2.73, 2.68, 2.66, 2.66, 2.65, 2.65, 2.6, 2.56, 2.56, 2.52, 2.52, 2.47, 2.43, 2.43, 2.39, 2.39, 2.35, 2.35, 2.31, 2.27, 2.27, 2.25, 2.25, 2.21, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19], 'pg_settings_random_page_cost': [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0], 'pg_settings_max_worker_processes': [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0], 'pg_settings_max_parallel_workers': [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0]}, 'io': {'SUM(pg_stat_database_tup_inserted': [74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0], 'SUM(pg_stat_database_tup_updated': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'process_open_fds': [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0], 'irate(pg_stat_database_xact_commit': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'irate(pg_stat_database_xact_rollback': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, 'memory': {'irate(node_disk_write_time_seconds_total': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'node_memory_MemAvailable_bytes': [468258816.0, 469819392.0, 468520960.0, 465346560.0, 461885440.0, 438071296.0, 476889088.0, 460292096.0, 463327232.0, 438063104.0, 441995264.0, 445128704.0, 449732608.0, 453677056.0, 435666944.0, 449884160.0, 446963712.0, 428564480.0, 443920384.0, 568770560.0, 572272640.0, 573341696.0, 553869312.0, 566128640.0, 552030208.0, 551911424.0, 589762560.0, 571658240.0, 590884864.0, 574300160.0, 572821504.0, 573337600.0, 570322944.0, 590577664.0, 577409024.0, 570724352.0, 579248128.0, 571662336.0, 575856640.0, 578465792.0, 574685184.0, 565133312.0, 568729600.0, 563625984.0, 581324800.0, 581017600.0, 576483328.0, 576876544.0, 576466944.0, 572772352.0, 565907456.0, 579497984.0, 546074624.0, 536088576.0, 417271808.0, 503992320.0, 508436480.0, 502521856.0, 501276672.0, 482934784.0, 606687232.0, 611500032.0, 599707648.0, 605954048.0, 603152384.0, 588668928.0, 597917696.0, 603873280.0, 601260032.0, 597393408.0, 600858624.0, 594878464.0, 585924608.0, 574898176.0, 600326144.0, 592023552.0, 591802368.0, 590430208.0, 596348928.0, 608690176.0, 590307328.0, 604463104.0, 565714944.0, 577732608.0, 398663680.0, 474562560.0, 481763328.0, 460161024.0, 473890816.0, 483729408.0, 500969472.0, 505593856.0, 524492800.0, 553545728.0, 549052416.0, 540053504.0, 551493632.0, 551342080.0, 524640256.0, 552914944.0, 547696640.0, 551858176.0, 526331904.0, 534683648.0, 535015424.0, 530735104.0, 533827584.0, 536539136.0, 539672576.0, 542396416.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0, 546803712.0], 'node_memory_Dirty_bytes': [905216.0, 917504.0, 1077248.0, 8192.0, 184320.0, 200704.0, 4096.0, 24576.0, 131072.0, 249856.0, 266240.0, 8192.0, 413696.0, 442368.0, 479232.0, 32768.0, 4096.0, 53248.0, 192512.0, 270336.0, 282624.0, 294912.0, 221184.0, 266240.0, 311296.0, 323584.0, 466944.0, 483328.0, 684032.0, 782336.0, 794624.0, 835584.0, 778240.0, 32768.0, 212992.0, 237568.0, 319488.0, 339968.0, 356352.0, 438272.0, 450560.0, 462848.0, 589824.0, 0.0, 188416.0, 204800.0, 274432.0, 8192.0, 4096.0, 225280.0, 237568.0, 294912.0, 454656.0, 471040.0, 512000.0, 544768.0, 630784.0, 655360.0, 667648.0, 385024.0, 126976.0, 225280.0, 372736.0, 389120.0, 421888.0, 405504.0, 483328.0, 499712.0, 512000.0, 483328.0, 233472.0, 303104.0, 253952.0, 315392.0, 356352.0, 393216.0, 471040.0, 487424.0, 503808.0, 450560.0, 462848.0, 487424.0, 311296.0, 372736.0, 319488.0, 327680.0, 397312.0, 450560.0, 942080.0, 974848.0, 1007616.0, 1048576.0, 262144.0, 376832.0, 397312.0, 131072.0, 237568.0, 262144.0, 278528.0, 356352.0, 372736.0, 385024.0, 499712.0, 548864.0, 565248.0, 585728.0, 503808.0, 24576.0, 143360.0, 184320.0, 212992.0, 212992.0, 212992.0, 212992.0, 212992.0, 212992.0, 212992.0, 212992.0, 212992.0, 212992.0, 212992.0], 'pg_stat_activity_count': [2.0, 6.0, 2.0, 5.0, 1.0, 3.0, 6.0, 4.0, 3.0, 2.0, 3.0, 3.0, 6.0, 2.0, 3.0, 8.0, 5.0, 3.0, 4.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'pg_settings_shared_buffers_bytes': [134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0, 134217728.0]}, 'network': {'node_sockstat_TCP_tw': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'node_sockstat_TCP_orphan': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'irate(node_netstat_Tcp_PassiveOpens': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'node_sockstat_TCP_alloc': [649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 649.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 250.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 250.0, 249.0, 249.0, 249.0, 252.0, 251.0, 250.0, 250.0, 250.0, 250.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 249.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0, 251.0], 'node_sockstat_TCP_inuse': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}}}], 'groupLabels': {'alertname': 'NodeMemSwapped'}, 'commonLabels': {'alertname': 'NodeMemSwapped', 'category': 'node', 'instance': 'node_exporter:9100', 'job': 'node_exporter', 'level': '2', 'severity': 'INFO'}, 'commonAnnotations': {'description': 'node:ins:swap_usage[ins=] = 0.71 > 1%\n', 'summary': 'INFO NodeMemSwapped @node_exporter:9100 0.71'}, 'externalURL': 'http://afdbeb1243fd:9093', 'version': '4', 'groupKey': '{}:{alertname="NodeMemSwapped"}', 'truncatedAlerts': 0}