package errors;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.RequiredArgsConstructor;

import java.util.List;
import java.util.Map;

@Data
@Builder
@AllArgsConstructor
@RequiredArgsConstructor

public class ErrorMessage {

    private String code;
    private List<Map<String, String>> mensajes;



}
