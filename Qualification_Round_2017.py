# Constant variables
videos = []
cache_size = 100

endpoints = [[100, 4] , [200 , 0] , [ 500 , 1]]


def check_valid_endpoints(endpoint_list):
    valid_endpoints = []
    for i in range(len(endpoint_list)):
        if list[i][1] != 0:
            valid_endpoints.append(i)
    return valid_endpoints


def check_valid_videos(videos):
    valid_videos = []
    for i in range(len(videos)):
        if videos[i] <= cache_size:
            valid_videos.append(i)
    return valid_videos

request = []
def get_request(dict ,videos):
    videos = check_valid_videos(videos)
    for elem in dict:
        for i in dict[elem]:
            for n in videos:
                if i == n:
                    request.append(dict[elem][i])


new_request = sorted(request)









def readfile(file):
    file_data = open(file, 'r')
    row1 = file_data.readline()
    nums = list(map(int, row1.split(" ")))

    endpoints = []
    no_vids = nums[0]
    no_endpoints = nums[1]
    no_request_descr = nums[2]
    no_cache_servers = nums[3]
    cache_capacity = nums[4]



    row2 = file_data.readline()
    nums2 = list(map(int, row2.split(" ")))
    vid_sizes = []
    for i in range(no_vids):
        vid_sizes.append(nums2[i])



    endpoint_dets = []


    for j in range(no_endpoints):
        row = file_data.readline()
        nums = list(map(int, row.split(" ")))
        # endpoint1_dets.append(nums[0])
        # endpoint1_dets.append(nums[1])
        endpoints.append(nums)

        cache_endpoint_descr = []
        for j in range(endpoints[j][1]):

            row = file_data.readline()
            nums = list(map(int, row.split(" ")))
            cache_endpoint_descr.append(nums)

        endpoint_dets.append(cache_endpoint_descr)

    endpoint_video_mapping = {}
    request_video = {}
    video_endpoint = {}
    for i in range(no_request_descr):
        row = file_data.readline()
        nums = list(map(int, row.split(" ")))
        video_request = {nums[0]:nums[2]}
        request_video.update({nums[2]:nums[0]})
        endpoint_video_mapping[nums[1]] = video_request

    print(vid_sizes)
    print(endpoints)
    print(endpoint_dets)
    print(endpoint_video_mapping)
    print(request_video)


readfile('input_file_data')