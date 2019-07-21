include "base.thrift"

namespace py DemoService

struct ARequest {
    1: optional base.Base Base,
    2: i64 a1,
    3: string a2
}

struct AResponse {
    1: base.BaseResp BaseResp,
    2: bool success
}

service DemoService {
    AResponse DemoInvoke(1: ARequest req)
}