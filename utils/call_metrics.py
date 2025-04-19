def compute_metrics(conversation):
    overtalk_duration = 0
    silence_duration = 0
    total_duration = float(conversation[-1]['etime']) - float(conversation[0]['stime'])

    for i in range(1, len(conversation)):
        prev = conversation[i-1]
        curr = conversation[i]

        if prev['etime'] > curr['stime']:
            overtalk_duration += prev['etime'] - curr['stime']
        else:
            silence_duration += curr['stime'] - prev['etime']

    return {
        'overtalk_pct': round((overtalk_duration / total_duration) * 100, 2),
        'silence_pct': round((silence_duration / total_duration) * 100, 2)
    }