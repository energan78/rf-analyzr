export interface SignalInfo {
    name: string;
    start: number;
    end: number;
    modulation: string;
    usage: string;
    manufacturer: string;
    channel: string;
    signal_type: string;
    codec: string;
    encryption: string;
    extra: Record<string, any>;
}

export interface SignalsResponse {
    signals: SignalInfo[];
}

export interface SignalsByFrequencyResponse {
    frequency: number;
    signals: SignalInfo[];
}
