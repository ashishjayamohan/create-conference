import requests

headers = {"accept": "*/*", "content-type": "application/x-protobuf", "accept-encoding": "gzip", "content-length": "468", "content-encoding": "gzip", "accept-language":" en-US,en;q=0.9", "user-agent": "datatransport/Unknown fllsupport/UNKNOWN apple/", "x-goog-api-key": "AIzaSyB4G40IhwotnuD26vAV-0PAxOVr5zn1BCc"}

data = r'''Ó
@"<16"16.2*522US:
iPhone13,2BenZcom.transact.mobileorderÿûø«ì02ê:J
iPhone13,2R)1:347274277294:ios:d312ead336dd2fb025583fbcom.transact.mobileorder80100000 ¨²16.2Â15.0ÈÐâ14B47b-20B71è ðúÍapple-platform/ios apple-sdk/20B71 appstore/true deploy/cocoapods device/iPhone13,2 fire-analytics/8.1.1 fire-install/8.1.0 fire-ios/8.1.0 firebase-crashlytics/8.1.0 os-version/16.2 swift/true xcode/14B47b xÿÁ÷ãËî	üã¦óªì02ç:J
iPhone13,2R)1:347274277294:ios:d312ead336dd2fb025583fbcom.transact.mobileorder80100000¨²16.2Â15.0ÈÐâ14B47b-20B71è ðúÍapple-platform/ios apple-sdk/20B71 appstore/true deploy/cocoapods device/iPhone13,2 fire-analytics/8.1.1 fire-install/8.1.0 fire-ios/8.1.0 firebase-crashlytics/8.1.0 os-version/16.2 swift/true xcode/14B47b xÿÁßî	 þü«ì0@úçËî	

@"<16"16.2*522US:
iPhone13,2BenZcom.transact.mobileorder®
? 26
À£óªì0 ú«ì0

ÚÄ	"com.transact.mobileorderx   þü«ì0@úçËî'''

x = requests.post("firebaselogging-pa.googleapis.com", headers=headers, data=data)

print(x.text)