import requests
kv={'user-agent':'Mozilla/5.0'}
url="https://www.amazon.cn/dp/B001BEFO0K/ref=s9_acsd_hps_bw_c2_x_2_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=H8BYP9TFDQR7DMSKEYEA&pf_rd_t=101&pf_rd_p=8ce85397-2447-41ba-bccf-eaf6c54d4a12&pf_rd_i=2330900071"
r=requests,get(url,headers=kv)
print(r.status_code)
