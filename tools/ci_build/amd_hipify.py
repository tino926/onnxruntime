#!/usr/bin/env python3

import os
import subprocess

contrib_ops_path = 'onnxruntime/contrib_ops'
core_ops_path = 'onnxruntime/core/providers'
training_ops_path = 'orttraining/orttraining/training_ops'

contrib_ops_files = [
                    # 'cuda_contrib_kernels.cc',
                    # 'cuda_contrib_kernels.h',
                    'activation/activations.cc',
                    'activation/activations.h',
                    'activation/activations_impl.cu',
                    'activation/activations_impl.h',
                    'bert/fast_gelu.cc',
                    'bert/fast_gelu.h',
                    # 'bert/fast_gelu_impl.cu',
                    'bert/fast_gelu_impl.h',
                    # 'math/bias_softmax.cc',
                    # 'math/bias_softmax.h',
                    # 'math/bias_softmax_impl.cu',
                    # 'math/binary_elementwise_ops.cc',
                    # 'math/binary_elementwise_ops.h',
                    # 'math/binary_elementwise_ops_impl.cu',
                    # 'math/binary_elementwise_ops_impl.h',
                    'math/fused_matmul.cc',
                    'layer_norm.cc',
                    'layer_norm.h',
                    'layer_norm_impl.cu',
                    'layer_norm_impl.h',
]

core_ops_files = [
                # 'cuda_allocator.cc',
                # 'cuda_allocator.h',
                # 'cuda_call.cc',
                # 'cuda_common.h',
                # 'cuda_execution_provider.cc',
                # 'cuda_execution_provider.h',
                # 'cuda_fence.cc',
                # 'cuda_fence.h',
                # 'cuda_fwd.h',
                # 'cuda_pch.cc',
                # 'cuda_pch.h',
                # 'cuda_provider_factory.cc',
                # 'cuda_utils.cu',
                # 'fpgeneric.cu',
                # 'gpu_data_transfer.cc',
                # 'gpu_data_transfer.h',
                'activation/activations.cc',
                'activation/activations.h',
                'activation/activations_impl.cu',
                'activation/activations_impl.h',
                # 'atomic/common.cuh',
                # 'cu_inc/binary_elementwise_impl.cuh',
                # 'cu_inc/common.cuh',
                'cu_inc/unary_elementwise_impl.cuh',
                'cu_inc/variadic_elementwise_impl.cuh',
                # 'math/binary_elementwise_ops.cc',
                # 'math/binary_elementwise_ops.h',
                # 'math/binary_elementwise_ops_impl.cu',
                # 'math/binary_elementwise_ops_impl.h',
                # 'math/binary_elementwise_ops_impl_functors.cuh',
                'math/clip_impl.cu',
                'math/clip_impl.h',
                'math/clip.cc',
                'math/clip.h',
                # 'math/gemm.cc',
                'math/gemm.h',
                # 'math/matmul.cc',
                'math/matmul.h',
                'math/softmax_impl.cu',
                'math/softmax_impl.cuh',
                # 'math/softmax.cc',
                'math/softmax.h',
                'math/unary_elementwise_ops_impl.cu',
                'math/unary_elementwise_ops_impl.h',
                'math/unary_elementwise_ops.cc',
                'math/unary_elementwise_ops.h',
                # 'math/variadic_elementwise_ops.cc',
                # 'math/variadic_elementwise_ops.h',
                # 'math/variadic_elementwise_ops_impl.cu',
                # 'math/variadic_elementwise_ops_impl.h',
                'math/variadic_elementwise_ops_tags.h',
                'multi_tensor/common.cuh',
                'nn/dropout.cc',
                'nn/dropout.h',
                'nn/dropout_impl.cu',
                'nn/dropout_impl.h',
                # 'reduction/reduction_functions.cu',
                # 'reduction/reduction_functions.h',
                # 'reduction/reduction_ops.cc',
                # 'reduction/reduction_ops.h',
                'reduction/reduction_utils.cuh',
                # 'shared_inc/cuda_call.h',
                'shared_inc/cuda_utils.h',
                # 'shared_inc/fast_divmod.h',
                # 'shared_inc/fpgeneric.h',
                'tensor/cast_op.cc',
                'tensor/cast_op.h',
                'tensor/concat_impl.cu',
                'tensor/concat_impl.h',
                'tensor/concat.cc',
                'tensor/concat.h',
                'tensor/expand_impl.cu',
                'tensor/expand_impl.h',
                'tensor/expand.cc',
                'tensor/expand.h',
                'tensor/gather_impl.cu',
                'tensor/gather_impl.h',
                # 'tensor/gather_nd_impl.cu',
                'tensor/gather_nd_impl.h',
                'tensor/gather_nd.cc',
                'tensor/gather_nd.h',
                'tensor/gather.cc',
                'tensor/gather.h',
                'tensor/identity_op.cc',
                'tensor/identity_op.h',
                'tensor/onehot.cc',
                'tensor/onehot.cu',
                'tensor/onehot.h',
                'tensor/reshape.cc',
                'tensor/reshape.h',
                'tensor/scatter_elements.cc',
                'tensor/scatter_elements.h',
                'tensor/scatter_elements_impl.cu',
                'tensor/scatter_elements_impl.h',
                'tensor/shape_op.cc',
                'tensor/slice_impl.cu',
                'tensor/slice_impl.h',
                'tensor/slice.cc',
                'tensor/slice.h',
                'tensor/split.cc',
                'tensor/split.h',
                'tensor/split_impl.cu',
                'tensor/split_impl.h',
                'tensor/squeeze.cc',
                'tensor/squeeze.h',
                # 'tensor/transpose_impl.cu',
                # 'tensor/transpose_impl.h',
                # 'tensor/transpose.cc',
                # 'tensor/transpose.h',
                'tensor/unsqueeze.cc',
                'tensor/unsqueeze.h',
                'tensor/where_impl.cu',
                'tensor/where_impl.h',
                'tensor/where.cc',
                'tensor/where.h',
]

training_ops_files = [
                    # 'cuda_training_kernels.cc',
                    # 'cuda_training_kernels.h',
                    # 'activation/activations_grad.cc',
                    'activation/activations_grad.h',
                    'activation/activations_grad_impl.cu',
                    'activation/activations_grad_impl.h',
                    'activation/bias_gelu_grad.cc',
                    'activation/bias_gelu_grad.h',
                    'activation/bias_gelu_grad_impl.cu',
                    'activation/bias_gelu_grad_impl.h',
                    'activation/gelu_grad_impl_common.cuh',
                    'collective/megatron.cc',
                    # 'collective/nccl_common.cc',
                    'collective/nccl_common.h',
                    'collective/nccl_kernels.cc',
                    'collective/nccl_kernels.h',
                    'controlflow/group.cc',
                    # 'loss/softmax_cross_entropy_loss_impl.cc',
                    'loss/softmax_cross_entropy_loss_impl.cu',
                    'loss/softmax_cross_entropy_loss_impl.h',
                    # 'loss/softmaxcrossentropy_impl.cc',
                    'loss/softmaxcrossentropy_impl.cu',
                    'loss/softmaxcrossentropy_impl.h',
                    'math/isfinite.cc',
                    'math/isfinite.cu',
                    # 'math/isfinite.cuh',
                    'math/isfinite.h',
                    'math/mixed_precision_scale.cc',
                    'math/mixed_precision_scale.cu',
                    'math/mixed_precision_scale.h',
                    'math/softmax_grad_impl.cu',
                    # 'math/softmax_grad.cc',
                    'math/softmax_grad.h',
                    'nn/dropout.cc',
                    'nn/dropout.h',
                    'nn/dropout_impl.cu',
                    'nn/dropout_impl.h',
                    'nn/layer_norm.cc',
                    'nn/layer_norm.h',
                    'nn/layer_norm_impl.cu',
                    'nn/layer_norm_impl.h',
                    # 'optimizer/adam.cc',
                    # 'optimizer/adam.cu',
                    'optimizer/adam.h',
                    'optimizer/common.cuh',
                    'optimizer/common.h',
                    'optimizer/gradient_control.cc',
                    'optimizer/gradient_control.cu',
                    'optimizer/gradient_control.h',
                    # 'optimizer/lamb.cc',
                    'optimizer/lamb.cu',
                    'optimizer/lamb.h',
                    'optimizer/sg.cc',
                    'optimizer/sg.cu',
                    'optimizer/sg.h',
                    'reduction/all.cc',
                    'reduction/all.cu',
                    'reduction/all.h',
                    'reduction/reduction_all.cc',
                    'reduction/reduction_all.cu',
                    'reduction/reduction_all.h',
                    # 'reduction/reduction_ops.cc',
                    'reduction/reduction_ops.h',
                    'tensor/concat.cc',
                    'tensor/concat.h',
                    'tensor/gather_elements_grad_impl.h',
                    'tensor/gather_grad_impl.cu',
                    'tensor/gather_grad_impl.h',
                    'tensor/gather_grad.cc',
                    'tensor/gather_grad.h',
                    # 'tensor/gather_nd_grad_impl.cu',
                    'tensor/gather_nd_grad_impl.h',
                    'tensor/gather_nd_grad.cc',
                    'tensor/gather_nd_grad.h',
                    'tensor/slice_grad.cc',
                    'tensor/slice_grad.h',
                    'tensor/split.cc',
                    'tensor/split.h',
                    'tensor/view.cc',
                    'tensor/view.h'
]

HIPIFY_PERL = '/opt/rocm/bin/hipify-perl'
FINDCODE = '/opt/rocm/bin/findcode.sh'


def hipify(src_file_path, dst_file_path):
    dst_file_path = dst_file_path.replace('cuda', 'rocm')
    dir_name = os.path.dirname(dst_file_path)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    with open(dst_file_path, 'w') as f:
        subprocess.run([HIPIFY_PERL, src_file_path], stdout=f)
    with open(dst_file_path) as f:
        s = f.read().replace('kCudaExecutionProvider', 'kRocmExecutionProvider')
        s = s.replace('CudaAsyncBuffer', 'RocmAsyncBuffer')
        s = s.replace('CudaKernel', 'RocmKernel')
        s = s.replace('ToCudaType', 'ToHipType')
        s = s.replace('CudaT', 'HipT')
        s = s.replace('CUDA_LONG', 'HIP_LONG')
        s = s.replace('CUDA_RETURN_IF_ERROR', 'HIP_RETURN_IF_ERROR')
        s = s.replace('CUDA_KERNEL_ASSERT', 'HIP_KERNEL_ASSERT')
        s = s.replace('CUDA_CALL', 'HIP_CALL')
        s = s.replace('SliceCuda', 'SliceRocm')
        s = s.replace('cuda', 'rocm')
        # s = s.replace('Cuda', 'Rocm')
        s = s.replace('CUDA', 'ROCM')

        s = s.replace('GPU_WARP_SIZE = 32', 'GPU_WARP_SIZE = 64')
        s = s.replace('std::exp', 'expf')
        s = s.replace('std::log', 'logf')
        s = s.replace('#include <cub/device/device_radix_sort.cuh>', '#include <hipcub/hipcub.hpp>')
        s = s.replace('#include <cub/iterator/counting_input_iterator.cuh>', '')
        s = s.replace('typedef half MappedType', 'typedef __half MappedType')
        # CUBLAS -> HIPBLAS
        s = s.replace('CUBLAS', 'HIPBLAS')
        s = s.replace('Cublas', 'Hipblas')
        s = s.replace('cublas', 'hipblas')

        # CURAND -> HIPRAND
        s = s.replace('CURAND', 'HIPRAND')
        s = s.replace('Curand', 'Hiprand')
        s = s.replace('curand', 'hiprand')

        # NCCL -> RCCL
        # s = s.replace('NCCL_CALL', 'RCCL_CALL')
        s = s.replace('#include <nccl.h>', '#include <rccl.h>')

        # CUDNN -> MIOpen
        s = s.replace('CUDNN', 'MIOPEN')
        s = s.replace('Cudnn', 'Miopen')
        s = s.replace('cudnn', 'miopen')
        # hipify seems to have a bug for MIOpen, cudnn.h -> hipDNN.h, cudnn -> hipdnn
        s = s.replace('#include <hipDNN.h>', '#include <miopen/miopen.h>')
        s = s.replace('hipdnn', 'miopen')
        s = s.replace('HIPDNN_STATUS_SUCCESS', 'miopenStatusSuccess')
        s = s.replace('HIPDNN', 'MIOPEN')

        # CUSPARSE -> HIPSPARSE
        s = s.replace('CUSPARSE', 'HIPSPARSE')

        # CUFFT -> HIPFFT
        s = s.replace('CUFFT', 'HIPFFT')
    with open(dst_file_path, 'w') as f:
        f.write(s)


def amd_hipify():
    cuda_path = contrib_ops_path + '/cuda/'
    hip_path = contrib_ops_path + '/rocm/'
    for file in contrib_ops_files:
        src_file_path = cuda_path + file
        dst_file_path = hip_path + file
        hipify(src_file_path, dst_file_path)

    cuda_path = core_ops_path + '/cuda/'
    hip_path = core_ops_path + '/rocm/'
    for file in core_ops_files:
        src_file_path = cuda_path + file
        dst_file_path = hip_path + file
        hipify(src_file_path, dst_file_path)

    cuda_path = training_ops_path + '/cuda/'
    hip_path = training_ops_path + '/rocm/'
    for file in training_ops_files:
        src_file_path = cuda_path + file
        dst_file_path = hip_path + file
        hipify(src_file_path, dst_file_path)


if __name__ == '__main__':
    amd_hipify()
