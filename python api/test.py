import argparse
import sys

# import 偵測電梯API lib
import elevatorAPI

def main(args):
    ip = args.ip
    # 'rtsp://admin:admin@192.168.101.100/Media/stream1'
    # 宣告一个变数为API的物件 同時設定初始畫面
    myele = elevatorAPI.ele(ip)

    # 类别方法compare可以与初始画面相比 输出0 电梯为空, 输出1 表示电梯不为空或是相机被移动过, 输出4 表示ip找不到camera
    # 輸入參數為CAMERA IP
    result = myele.compare(ip)
    print('elevator output :', result)

    # 类别方法get_initial_status 可以返回初始畫面是否因為錯誤而為空 true：表示初始畫面為空  false:表示初始畫面不為空
    # 輸入參數為CAMERA IP
    initial_status = myele.get_initial_status()
    print('is initial null ? ', initial_status)

    # 类别方法reinitial 可以重新設置初始畫面 ,鏡頭若被動到需要重新調整可以使用
    # 輸入參數為CAMERA IP
    myele.reinitial(ip)


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str,
                        help='Your ipcamera IP', default='rtsp://admin:admin@192.168.101.100/Media/stream1')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))