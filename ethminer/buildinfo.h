#ifndef ETHMINER_BUILDINFO_H__
#define ETHMINER_BUILDINFO_H__

struct ethminer_buildinfo
{
    const char* project_version;
    const char* system_name;
    const char* build_type;
    const char* compiler_id;
    const char* project_name_with_version;
};

inline struct ethminer_buildinfo* ethminer_get_buildinfo()
{
    static struct ethminer_buildinfo st = {
        "ce52c74021b6fbaaddea3c3c52f64f24e39ea3e9",
        "",
        "gyp",
        "",
        "ethminer/ce52c74021b6fbaaddea3c3c52f64f24e39ea3e9",
    };
    return &st;
}

#endif  // ETHMINER_BUILDINFO_H__
