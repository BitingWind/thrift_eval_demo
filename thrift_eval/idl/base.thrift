namespace py base

struct Base {
    1: string LogID = "",
    2: string Caller = "",
}

struct BaseResp {
    1: string StatusMessage = "",
    2: i32 StatusCode = 0,
    3: optional map<string, string> Extra,
}
