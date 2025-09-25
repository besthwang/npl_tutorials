import torch
import numpy as np

def as_strided_custom(x, size, stride, storage_offset=0):
    """
    간단한 as_strided 흉내내기 (numpy 버전)

    x: 원본 1차원 numpy 배열 (메모리)
    size: 결과 텐서 shape (tuple)
    stride: 각 차원 이동 시 메모리 점프 크기 (tuple)
    storage_offset: 메모리 시작 위치
    """
    # 결과 shape에 맞는 인덱스 좌표 생성
    idx = np.indices(size)  # 각 좌표의 인덱스 그리드
    offset = storage_offset

    # 좌표 * stride 를 더해 메모리 인덱스 계산
    mem_index = offset + sum(idx[d] * stride[d] for d in range(len(size)))

    # 원본 메모리에서 값 추출
    return x[mem_index]

def as_strided_manual(x: torch.Tensor, size, stride, storage_offset=0):
    """
    torch.as_strided를 흉내내는 완전 파이썬 구현 (복사본 반환)

    Args:
        x (torch.Tensor): 입력 텐서 (임의 차원 가능)
        size (tuple): 결과 shape
        stride (tuple): 각 차원별 stride (메모리 점프 크기)
        storage_offset (int): 시작 위치 (default=0)

    Returns:
        torch.Tensor: 복사된 결과 텐서
    """
    # 결과 좌표 그리드 생성 (예: size=(2,3) -> 좌표 shape=(2,3))
    idx = torch.cartesian_prod(*[torch.arange(s) for s in size])
    # idx shape = (모든 좌표 수, 차원 수)

    # 메모리 인덱스 계산: offset + Σ (좌표[d] * stride[d])
    mem_index = storage_offset + sum(idx[:, d] * stride[d] for d in range(len(size)))

    # 원본 데이터를 flatten 해서 인덱싱
    flat = x.reshape(-1)
    values = flat[mem_index]

    # 원하는 모양으로 reshape
    return values.view(size)

def unfold(x, dim, size, step):
    dim_size = x.shape[dim]
    assert size <= dim_size

    new_size = (dim_size - size) // step + 1

    new_shape = list(x.shape)
    new_shape[dim] = new_size
    new_shape.insert(dim + 1, size)

    strides = list(x.stride())
    new_strides = strides.copy()
    new_strides[dim] *= step
    new_strides.insert(dim + 1, strides[dim])

    return as_strided_manual(x, new_shape, new_strides)
    #return x.as_strided(new_shape, new_strides)

if __name__ == "__main__":
    test = torch.arange(0,100).reshape((2,2,5,5))
    x1 = unfold(test,2,5,1)
    x2 = test.unfold(2,3,1)
    print(x2)

    # 예제: 3x3 행렬
    #base = np.arange(1, 10)  # [1..9]
    # x = base.reshape(3, 3)
    # y = as_strided_custom(base, size=(2, 2), stride=(3, 1))
    # print("\nstride=(3,1), size=(2,2):\n", y)