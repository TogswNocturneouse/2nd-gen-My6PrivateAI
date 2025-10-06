import SwiftUI
import Combine

struct ConsoleView: View {
    @State private var logs: [String] = []
    let wsURL = URL(string: "ws://localhost:8000/ws/logs")!

    var body: some View {
        ScrollView {
            ForEach(logs, id: \.self) { line in
                Text(line).font(.system(.body, design: .monospaced))
            }
        }.onAppear {
            connectWebSocket()
        }
    }

    func connectWebSocket() {
        let task = URLSession.shared.webSocketTask(with: wsURL)
        task.resume()
        receive(task)
    }

    func receive(_ task: URLSessionWebSocketTask) {
        task.receive { result in
            switch result {
            case .success(let message):
                if case let .string(text) = message {
                    DispatchQueue.main.async {
                        logs.append(text)
                    }
                }
                self.receive(task)
            case .failure(let error):
                print("WS error: \(error)")
            }
        }
    }
}